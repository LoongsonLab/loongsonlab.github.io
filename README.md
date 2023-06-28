# Website for the Loongson Lab

Deployed at https://loongsonlab.github.io/.

The setup is modified from https://cmudig.github.io. Thanks to `Data Interaction Group at CMU`.

## Run

Install Jekyll dependencies with `bundle`. To start this page, run `bundle exec jekyll serve --livereload`.

## Run with Docker

```
docker run \
  --volume="$PWD:/srv/jekyll" \
  -p 4000:4000 -p 35729:35729 \
  -it jekyll/jekyll \
  jekyll serve --livereload
```

## Add Content

To add specific content, follow the README guides in the corresponding directories:

* [Add a person](_people)
* [Add a publication](_publications)
* [Add a post](_posts)
* [Add a course](_courses)
* [Add a research area](_research)