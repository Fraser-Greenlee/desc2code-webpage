



def reset_oldest():
    oldest = db.select('users',order='age desc',limit=1)[0]
    oldest['winner'] = True
    db.update('users',oldest,where='id='+str(oldest['id']))










def resetrows(oldest):
    return oldest





#
