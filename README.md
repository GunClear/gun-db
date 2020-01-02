# gun-db
List of Firearm Makes, Models, and Variants

## Structure

Database is structured as JSON documents, organized according to the following:
```
{manufacturer}/
  {model}/
    {model number}.json
```

`{manufacturer}` is the full legal name of the maker of the particular model,
without any corporation-specific identification such as `inc.` or `llc.`

`{model}` is the *base model* of a particular class of models that a manufacturer makes.
Variants such as caliber types, barrel lengths, fire modes, etc. go inside the `json` files
that describe them via their `{model number}`.

## Contributing

If you see something wrong or missing, please feel free to add them via PR.
If you feel something is not public information free for common use (according to CC-1.0),
please add an issue or contact us at [admin@gunclear.io](mailto:admin@gunclear.io).
