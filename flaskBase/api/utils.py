def get_fields(request, required_fields=None, allowed_fields=None):
    fields = {}
    fields_error = None
    # First args
    for field in request.args:
        if (allowed_fields and field in allowed_fields) or allowed_fields is None:
            fields[field] = request.args[field]

    # Then form
    for field in request.form:
        if (allowed_fields and field in allowed_fields) or allowed_fields is None:
            fields[field] = request.form[field]

    # Then json
    try:
        request.get_json()
    except Exception:
        pass
    else:
        if request.get_json():
            for field in request.get_json():
                if (allowed_fields and field in allowed_fields) or allowed_fields is None:
                    fields[field] = request.get_json()[field]

    if required_fields:
        for field in required_fields:
            if field not in fields:
                return {}, {'message': 'Field `%s` is required' % field}

    return fields, fields_error
