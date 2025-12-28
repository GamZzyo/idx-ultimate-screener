export async function GET() {
  const backendUrl = process.env.BACKEND_URL;

  if (!backendUrl) {
    return Response.json(
      { error: "BACKEND_URL not set" },
      { status: 500 }
    );
  }

  const res = await fetch(`${backendUrl}/scan`, {
    cache: "no-store"
  });

  const data = await res.json();
  return Response.json(data);
}
