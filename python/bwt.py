import sys
import os
import tempfile


class BWT:
    def __init__(self, n):
        self.n = n
        self.alphabet_dict = {}
        self.alphabet_reverse_dict = {}
        self.input_int_list = []
        self.output_int_list = []
        self.bwt = []

    def encode(self, string_list):
        letters = sorted(list(set(string_list)))
        count = 1
        for s in letters:
            self.alphabet_dict[s] = count
            self.alphabet_reverse_dict[count] = s
            count = count+1

        for s in string_list:
             self.input_int_list.append(self.alphabet_dict[s])
        return self.input_int_list

    def suffixArray(self):
        fin = "in.txt"
        fout = "out.txt"

        tf_in = open(fin, "w")
        for i in range(self.n):
            tf_in.write("%d\n" % self.input_int_list[i])
        tf_in.write("0")
        tf_in.close()

        "needs to be improved, obviously"
        os.system("../c/sarray %s %s %d" % (fin, fout, self.n + 1))

        tf_out = open(fout, "r")
        for i in range(self.n + 1):
            self.output_int_list.append(int(tf_out.readline().strip()))
        tf_out.close()
        return self.output_int_list


    def computeBWT(self, string_list):
        self.encode(string_list)
        self.suffixArray()

        for i in self.output_int_list:
             if i > 0 and i < self.n:
                self.bwt.append(string_list[i-1])

        return self.bwt

#just for testing
def suffixArray(s):
    satups = sorted([(s[i:], i) for i in xrange(0, len(s)+1)])
    return map(lambda x: x[1], satups)


if __name__ == "__main__":
    string = sys.argv[1]
    string_list = list(string)

    bwt = BWT(len(string_list))
    bwt_of_string = bwt.computeBWT(string_list)

    out_str = ""
    for s in bwt_of_string:
        out_str = "%s%s"%(out_str, s)

    print"\n%s"%out_str

