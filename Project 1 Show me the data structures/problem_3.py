import sys
"""
Inspired from https://github.com/viralj/nd256_project2/blob/master/solution_3.py

Basically I tried tp use a tree first, but I could not figure out how to merge two trees, which
the visualizations seemed to imply. In the forum some people seems to head a heaq module in python,
but this seems to make it too easy. Googling on the issue, I found the github above. I understood its solution
and was able to encode it more efficiently. The size of their decoded data is 69, mine is 40, i.e. considerably
smaller. 

"""


def huffman_encoding(data):
    """
    Takes a string as input
    returns a tree and encoded data
    """
    freq_table = dict()
    key2code = dict()
    encoded_data = ""
    delimiter = "1"
    # compute frequencies
    for symbol in data:
        if symbol in freq_table:
            freq_table[symbol] = freq_table[symbol]+1
        else:
            freq_table[symbol] = 1

    for tupple in sorted(freq_table.items(), key=lambda tupple: tupple[1], reverse=True):
        key2code.update({tupple[0]: delimiter})
        delimiter = delimiter+"0"

    for symbol in data:
        encoded_data= encoded_data+key2code[symbol]


    return encoded_data, key2code

def huffman_decoding(encoded_data,key2code):
    tmp = encoded_data.split(sep="1")
    list_of_inputs =[]
    for element in tmp:
        list_of_inputs.append("1"+element)

    decoded_data = ""
    code2key = {v: k for k, v in key2code.items()} ## this works because by construction values are unique.

    for element in list_of_inputs:
        decoded_data = decoded_data+code2key[element]

    decoded_data = decoded_data[1:]
    return decoded_data


data = "The bird is the word"




if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
