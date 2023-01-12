export interface Env {
  PEXELS: string
}

type PexelsQuery = { photos: { src: { large: string; large2x: string } }[] }

const BadRequest = () => new Response('Bad Request', { status: 400 })
const NotFound = () => new Response('Not Found', { status: 404 })

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const needle = new URL(request.url).pathname.slice(1)

    if (!needle.length) return BadRequest()

    const { photos } = await fetch(`https://api.pexels.com/v1/search?query=${needle}&per_page=80`, {
      headers: { Authorization: env.PEXELS },
    }).then((r) => r.json<PexelsQuery>())

    if (!photos.length) return NotFound()
    const random = photos[Math.floor(Math.random() * photos.length)]
    return new Response(random.src.large2x)
  },
}
