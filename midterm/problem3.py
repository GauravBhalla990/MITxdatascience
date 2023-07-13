def song_playlist(songs, max_size):
    srm = max_size #size remaining
    nms = []
    # if first name good
    if((songs[0][2]) <= max_size):
        srm -= songs[0][2]
        nms.append(songs[0][0])
    else:
        return []
    
    
    mdsg = songs[1:] # moded songs list
    while(srm > 0 and mdsg):
        min = mdsg[0]
        for i in range(len(mdsg) - 1):
            if(mdsg[i + 1][2] < min[2]):
                min = mdsg[i + 1]
            elif(mdsg[i + 1][2] == min[2]):
                if (mdsg[i + 1][1] > min[1]):
                    min = mdsg[i + 1]
        srm -= min[2]
        if(srm < 0):
            break
        mdsg.remove(min)
        nms.append(min[0])
    
    return nms

sng = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 6.9)]
mae = 11

print(song_playlist(sng,mae))

