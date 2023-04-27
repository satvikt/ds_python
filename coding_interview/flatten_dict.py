input_dict = {
    "foo": "hi",
    "bar": "zed",
    "flup": {
        "yar": "xe",
        "zip": {"hop": "lrp"}
    }
}

output = {
    "foo": "hi",
    "bar": "zed",
    "flup_yar": "xe",
    "flup_zip_hop": "lrp"
}

# Code:
output_dict = dict()
def flatten_dict(input_dict, output_dict, old_key):

    for key, value in input_dict.items():
        combined_key = old_key + "_" + key if old_key else key
        if type(value)  == dict:
            flatten_dict(value, output_dict, combined_key)
        else:
            output_dict[combined_key] = value
    return output_dict


out = flatten_dict(input_dict, output_dict, "")

print(out)