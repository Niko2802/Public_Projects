converters_map = {
    "kg>g": lambda x: x * 1000
}

def converters(fr, to):
    conv_name = fr + ">" + to
    def worker(val):
        return converters_map[conv_name](val)
    return worker 


converter = converters("kg", "g")
print(converter(10))
