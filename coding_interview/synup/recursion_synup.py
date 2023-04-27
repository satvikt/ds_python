
input_dict = {
    "foo": "foo1",
    "bar": "bar2",
    "baz": {
        "foo1": "bar1",
        "bar2": {
            "baz3": "bar4"
        }
    }

}


output_dict = {
    "foo": "foo1",
    "bar": "bar2",
    "baz_foo" : "bar",
    "baz_bar_baz":"bar"
}


def recursive(input_dict, output):
    for key in input_dict:
        if type(input_dict[key]) is not dict:
            output[key] = input_dict[key]
        else:
            # combined_key =
            recursive(input_dict[key], output)


# def

if __name__ == "__main__":
    output = dict()
    recursive(input_dict, output)