from datetime import timedelta

def get_waktu_hh_mm_ss(sec):
    # create timedelta and convert it into string
    td_str = str(timedelta(seconds=sec))
    print("Waktu dalam Detik:", sec)

    # split string into individual component
    x = td_str.split(':')
    print("Time in hh:mm:ss:", x[0], 'Jam', x[1], 'Menit', x[2], 'Detik')

get_waktu_hh_mm_ss(3340)
