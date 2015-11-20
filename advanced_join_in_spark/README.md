from operator import add

show_views_file = sc.textFile("input/join2_gennum*")

# have lines of show, # of views
def split_show_views(line):
    s = line.split(",")
    return (s[0], int(s[1]))

show_views = show_views_file.map(split_show_views)

show_channel_file = sc.textFile("input/join2_genchan?.txt")

# have lines of show,channel
def split_show_channel(line):
    s = line.split(",")
    return (s[0],s[1])

show_channel = show_channel_file.map(split_show_channel)

joined_dataset = show_views.join(show_channel)

# from ("Foo Show", ("12345", "NBC")) we just want "NBC", "12345"
def extract_channel_views(show_views_channel):
    return (show_views_channel[1][1], show_views_channel[1][0])

# only want counts for "BAT" network
bat_only = joined_dataset.filter(lambda v: v[1][1] == "BAT")

def huh(v):                                   
    return int(v[0])

bat_only_views = bat_only.combineByKey(huh, add, add)

bat_only_views.values().sum()