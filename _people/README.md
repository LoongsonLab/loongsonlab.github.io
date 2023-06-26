# Adding a person

Create a new `KEY` folder in `_people` with a unique name for you.
Then in the folder, you can create each language file by using `index.LANG.md`.
Finally, fill it with the following content.

```md
---
layout: people
name: ...
image: /assets/people/....jpg
role: PhD Student
blog: https://www.baidu.com
email: example@example.com
github: https://www.baidu.com
alumni: true/false
alumni_since: XXXX (when alumni: true)
advisors:
    - AdvisorFirstName AdvisorLastName
date: YYYY-MM-DD
permalink: people/KEY
lang: zh/en
---

Your context...
```

We have the following roles: `Professor`, `Asst. Professor`, `PhD Student`, `Masters Student`, `Undergraduate Student`, `Visiting Student` and `Postdoc`. You can also add a new role if it makes sense (`roles` in file `team/index.LANG.html`).

Add a picture, add it to [the assets directory](../assets/people) with around `300x300` pixels as a JPEG image. The height and width of the image should be equal, so it is a square.

Once someone leaves the group, change `alumni` to `true` and add `alumni_since: XXXX` to make them as alumni.

Please send a pull request with the changes and an admin will merge it.
