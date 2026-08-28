// Cloudflare Pages Function for newsletter subscription
// Routes to: POST /api/subscribe
export async function onRequestPost({ request }: { request: Request; env?: any }) {
  try {
    const data = await request.json() as { email?: string };
    const email = data?.email?.trim();

    if (!email || !email.includes('@')) {
      return new Response(
        JSON.stringify({
          success: false,
          message: '请输入有效的邮箱地址',
        }),
        {
          status: 400,
          headers: { 'Content-Type': 'application/json' },
        }
      );
    }

    // Provider Integration Placeholder (e.g. Buttondown, Loops, Resend, ConvertKit)
    // Example:
    // if (env.NEWSLETTER_API_TOKEN) {
    //   await fetch('https://api.buttondown.email/v2/subscribers', {
    //     method: 'POST',
    //     headers: {
    //       'Authorization': `Token ${env.NEWSLETTER_API_TOKEN}`,
    //       'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({ email })
    //   });
    // }

    return new Response(
      JSON.stringify({
        success: true,
        message: '🎉 订阅成功！感谢关注，每日 AI 精选将准时送达。',
      }),
      {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      }
    );
  } catch (error) {
    return new Response(
      JSON.stringify({
        success: false,
        message: '服务器繁忙，请稍后再试',
      }),
      {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      }
    );
  }
}
