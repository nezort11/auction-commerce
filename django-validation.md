**Important note**: direct model instance manager.`create()`/`save()` doesn't validate (run instance.`full_clean()`).
**Only form validate instance** (calls instance.`full_clean()`).

ModelForm validation process (Form + Model instance):

1. `form.is_valid()`
2. `form.errors()`
3. `form.full_clean()` - populate errors and cleanded_data
    1. `form._clean_fields()` - (form.fields == model.fields)
        - `field.clean()`
            1. `field.to_python()`
            2. `field.validate()`
            3. `field.run_validators()`
    2. `form._clean_form()`
        - `form.clean()`
    3. `form._post_clean()` - populate instance with cleaned_data
        - `instance.full_clean()` - validate instance (model + cleaned_data)
            1. `instance.clean_fields()`
                - `field.clean()`
                    1. `field.validate()`
                    2. `field.run_validators()`
            2. `instance.clean()`
        - `form.validate_unique()`
            1. `instance.validate_unique()`
4. `form.save()`
    - `form.instance.save()`

Model object validation:

- `model.full_clean(validate_unique=True)`
    1. `model.clean_fields()`
    2. `model.clean()` - pass
    3. `model.validate_unique()`
