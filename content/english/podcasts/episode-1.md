---
title: "Podcast Episode Title"
date: 2024-10-26
description: "Brief description of the podcast episode."

---

## Listen Here

{{ if .Params.embed_url }}
<iframe src="{{ .Params.embed_url }}" width="100%" height="200" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
{{ end }}

## Listen to the Audio

{{< audio src="podcast-1.mp3" >}}  <!-- Use this if in Page Bundle -->