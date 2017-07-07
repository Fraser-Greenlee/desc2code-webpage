




def give_reward():
    select oldest user
    oldest = db.select('users',order='age desc',limit=1)[0]
    oldest['winnder'] = True
    update user with oldest
    db.update('users',where='id='+str(oldest['id']))
