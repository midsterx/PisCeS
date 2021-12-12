import h5py

def print_attrs(name, obj):
    print(name)
    for key, val in obj.attrs.items():
        print("    %s: %s" % (key, val))


filename = "ctc_lstm.h5"

h5 = h5py.File(filename,'r')
h5.visititems(print_attrs)
h5.close()
