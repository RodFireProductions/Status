# Status

My personal status updater. This site and system relies on Jekyll and Python.

Features:
- [HTML Journal](https://journal.miso.town/) compliant formatting (allows for Atom feed).
- The option to add an image to a status update.
- Different color scheme options for individual statuses.

## Updating Status

Run `Update.py` to update status. Make sure to change `site_url` to the url you'll be using.

To update the status and push it via Git, you'll have to change the directory listed in `Status Update.bat` and then run it.

## Running The Site

```
> cd site
> bundle exec jekyll serve
```

http://localhost:4000
