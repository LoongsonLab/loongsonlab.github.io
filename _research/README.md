# Adding a research area

Create a new `KEY` folder in `_research` with a unique name for you.
Then in the folder, you can create each language file by using `index.LANG.md`.
Finally, fill it with the following content.
Note that, `construct` is used to mark this page is under construction.

## Create the Markdown file

```md
---
layout: research
title: ...
description: ...
advisors:
  - advisor1
  - advisor2
  - ...
maintainers:
  - maintainer1
  - maintainer2
  - ...
contributors:
  - contributor1
  - contributor2
  - ...
date: YYYY-MM-DD
permalink: research/KEY
lang: zh/en
construct: true/false (optional is false)
index_hide: true/false (optional is false)
---

## Something...
...
```

The `title` and `description` will show at the top of the page. Besides that, they also show on the index of the website.
You also need to make sure the `description` cannot be too long (or the page may be a little ugly).
The `advisors`, `maintainers` and `contributors` can be eliminated, but we recommend you add them correctly.

Please send a pull request with the changes and an admin will merge it.

Also, if you want to create each group in a team, use `index_hide`. Then the group information will not show on the index page.

Make sure on each page, you need use `{% link _research/heterogeneous/thread-level-speculation/index.zh.md %}` to generate
the link URL.
You can get more information [here](https://jekyllrb.com/docs/liquid/tags/#links).
For example:

```md
[Link]({% link _research/*.md %})
```
