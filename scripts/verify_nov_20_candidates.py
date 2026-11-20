"""Strict GET verification for the 2026-11-20 issue. Run before generation."""
from pathlib import Path
import collections,concurrent.futures,datetime,hashlib,json,subprocess,sys,threading,time
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'scripts/candidates-2026-11-20.json'
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
lock=threading.Lock()
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(task):
 kind,url=task
 agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36' if 'woshipm.com' in url else UA
 cmd=['curl','-sSL','--max-time','35','--retry','1','-A',agent,'-o','/dev/null','-w','%{http_code}\t%{content_type}\t%{url_effective}',url]
 if any(host in url for host in ['woshipm.com','wzbj1616.com']):cmd[1:1]=['--noproxy','*']
 try:
  if 'woshipm.com' in url:
   with lock:time.sleep(.8);r=subprocess.run(cmd,capture_output=True,text=True,timeout=80)
  else:r=subprocess.run(cmd,capture_output=True,text=True,timeout=80)
  parts=r.stdout.split('\t',2);code=parts[0];ctype=parts[1] if len(parts)>1 else '';final=parts[2] if len(parts)>2 else ''
  ok=r.returncode==0 and code=='200' and (kind!='MEDIA' or ctype.startswith('image/'))
  return dict(kind=kind,url=url,status=code,content_type=ctype,final_url=final,ok=ok)
 except Exception as e:return dict(kind=kind,url=url,status='ERROR',ok=False,error=str(e))
def main():
 rows=json.loads(DATA.read_text());used=json.loads((ROOT/'scripts/all-used-urls.json').read_text())
 counts=collections.Counter(x['category'] for x in rows);pins=collections.Counter(x['category'] for x in rows if x['pinned'])
 assert len(rows)==36 and len(counts)==9 and set(counts.values())=={4},counts
 assert all(pins[c]==1 for c in counts),pins
 # Normalize superficial URL differences as well as checking exact strings.
 norm=lambda u:u.strip().rstrip('/').replace('http://','https://')
 previous={norm(u) for u in used};urls=[norm(x['url']) for x in rows]
 duplicates=[x for x in urls if x in previous]
 assert not duplicates and len(set(urls))==36,duplicates
 print('PASS: 0 duplicates against global used database.',flush=True)
 tasks=[(kind,x[field]) for x in rows for kind,field in [('URL','url'),('MEDIA','media')]]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  results=[]
  for result in pool.map(check,tasks):
   results.append(result);print(('OK' if result['ok'] else 'FAIL'),result['kind'],result['status'],result['url'],flush=True)
 report=dict(date='2026-11-20',checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),candidate_sha256=digest(DATA),used_sha256=digest(ROOT/'scripts/all-used-urls.json'),previous_url_count=len(used),category_counts=dict(counts),duplicates=duplicates,endpoints=results,passed=all(r['ok'] for r in results))
 (ROOT/'scripts/verification-2026-11-20.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 if not report['passed']:sys.exit(1)
 print('SUCCESS: ALL 36 items and their media returned HTTP 200/OK!')
if __name__=='__main__':main()
