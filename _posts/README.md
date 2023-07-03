# Adding a post

Create a new `KEY.md` file in the `_posts` directory with the date and title in the name. Learn more about posts in [the Jekyll docs](https://jekyllrb.com/docs/posts/).
Also, do not forget to create an English version to `_post/en/KEY.md`.

You can create a Markdown file like below:

```md
---
layout: post
title: ...
date: 2023-06-29 14:41:00 +0800 (optional)
studyLink: https://... (optional)
excerpt_separator: <!--more--> (optional)
side_image: "/assets/posts/*.png" (optional)
side_image_alt: ... (optional)
author: (optional)
  - ...
  - ...
lang: zh/en
---

## Title

...

<!--more-->

...
```

* If you want to add a participant link, you can add `studyLink` link.
* If you want to add a side image, you can add `side_image` and `side_image_alt`.
* If you want to give post time, you can add `date` field.
* `excerpt_separator` is used to define a label. All the text above the label will be treated as an excerpt.
