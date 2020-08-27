def bytenize(hex_stream):
	
    ret = [hex_stream[i:i+8] for i in range(0, len(hex_stream), 8)]
    
    return '_'.join(ret)

if
