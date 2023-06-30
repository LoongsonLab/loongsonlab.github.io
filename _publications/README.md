# Adding a publication

## Create the Markdown file

Create a new `KEY` folder in the `_publications` directory. The key for the filename should be `YEAR-TITLE` where title is a short key for your paper. Then in the folder, you can create each language file by using `index.LANG.md`.
Finally, Complete the file with the following basic format. Note that `permalink` needs to change the `KEY` to the folder name.\
Note that, `construct` is used to mark this page is under construction.

```md
---
layout: publication
year: ...
title: "..."
poster: /assets/.../*.png
thumb: /assets/.../*_thumb.png
authors:
  - ...
permalink: publications/KEY
lang: zh/en

doi: ...
short_doi: ...
osf: ...
type:
  - ...
venue: ...
venue_location: ...
venue_tags:
  - ...
venue_url:
tags:
  - ...
awards:
  - ...
tweet: "..."

blog: https://...
link: https://...
pdf: ...
recording: ...
slides: ...
construct: true/false
---
## Abstract

...

```

Only the properties in the first block(the under list) are required. The rest is optional but encouraged (where it makes sense).

```md
layout: publication
year: ...
title: "..."
poster: /assets/.../*.png
thumb: /assets/.../*_thumb.png
authors:
  - ...
permalink: publications/KEY
lang: zh/en

```

## Add a poster and thumbnail image

Add a poster and thumbnail image to `assets/publications/` in png format. It's important that we keep download sizes small. Please use https://tinypng.com/ to reduce the file sizes of all images.

The poster image should be at least 1920 pixels wide and wider than tall. Name your poster image `KEY.png`.

The thumbnail may have any aspect ratio but should be recognizable when shown as a small image. The thumbnail should be at least 600 pixels wide or tall. Name your thumbnail `KEY_thumb.png`. You can programmatically achieve this with `mogrify -resize 600x600^ *_thumb.png`.

Also, **do not forget** to put these pieces of information(`KEY.png` and `KEY_thumb.png`) into the corresponding area(`poster` and `thumb`).
