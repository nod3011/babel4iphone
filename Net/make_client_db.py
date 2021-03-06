# This file is part of babel4iphone.

# Copyright (C) 2009 Giovanni Amati <amatig@gmail.com>

# babel4iphone is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# babel4iphone is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with babel4iphone.  If not, see <http://www.gnu.org/licenses/>.


from db import Database

if __name__ == "__main__":
    # questo codice permette di creare un db solo delle info dei character per il client
    import os
    
    fname = "../Babel/gameDB.sqlite"
    try:
        os.remove(fname)
        print "Rimosso il vecchio database client."
    except:
        print "Il database client non esiste."
    
    s = Database()
    d = Database(fname)
    print "Creato nuovo database client."
    
    sql = 'CREATE TABLE "type" ("id" VARCHAR(25) PRIMARY KEY  NOT NULL ,"hp" CHAR,"mp" CHAR,"str" CHAR,"dex" CHAR,"vit" CHAR,"agi" CHAR,"int" CHAR,"mnd" CHAR)'
    if d.execute(sql):
        print "Creata tabella type."
        
        check = False
        for r in s.select("*", "type"):
            r = ["'%s'" % v for v in r]
            if not d.insert("type", r):
                check = True
        
        print "Database client popolato con le entry..."
        for r in d.select("*", "type"):
            print r
        if check:
            print "ERRORE: Alcuni type possono non essere stati inseriti!!!"
    else:
        print "Impossibile creare tabella type."
    
    sql = 'CREATE TABLE "scale" ("id" CHAR PRIMARY KEY  NOT NULL ,"scaleHP" REAL DEFAULT 0 ,"baseHP" REAL DEFAULT 0 ,"scaleHPXXX" REAL DEFAULT 0 ,"scaleMP" REAL DEFAULT 0 ,"baseMP" REAL DEFAULT 0 ,"scaleSTATS" REAL DEFAULT 0 ,"baseSTATS" REAL DEFAULT 0 )'
    if d.execute(sql):
        print "Creata tabella scale."
        
        check = False
        for r in s.select("*", "scale"):
            r[0] = "'%s'" % r[0]
            if not d.insert("scale", r):
                check = True
        
        print "Database client popolato con le entry..."
        for r in d.select("*", "scale"):
            print r
        if check:
            print "ERRORE: Alcuni scale possono non essere stati inseriti!!!"
    else:
        print "Impossibile creare tabella scale."
    
    sql = 'CREATE TABLE "skill" ("id" VARCHAR(25) PRIMARY KEY  NOT NULL , "desc" TEXT, "mp_cost" INTEGER DEFAULT 0, "attribute" VARCHAR(25), "duration" INTEGER DEFAULT 0, "aoe" BOOL DEFAULT 0, "passive" BOOL DEFAULT 0)'
    if d.execute(sql):
        print "Creata tabella skill."
        
        check = False
        for r in s.select("*", "skill"):
            r[0] = "'%s'" % r[0]
            r[1] = "'%s'" % r[1]
            r[3] = "'%s'" % r[3]
            if not d.insert("skill", r):
                check = True
        
        print "Database client popolato con le entry..."
        for r in d.select("*", "skill"):
            print r
        if check:
            print "ERRORE: Alcune skill possono non essere stati inseriti!!!"
    else:
        print "Impossibile creare tabella skill."
    
    sql = 'CREATE TABLE "skill_set" ("id" INTEGER PRIMARY KEY  NOT NULL ,"type_id" VARCHAR(25) NOT NULL ,"skill_id" VARCHAR(25) NOT NULL ,"level" INTEGER DEFAULT 1 )' 
    if d.execute(sql):
        print "Creata tabella skill_set."
        
        check = False
        for r in s.select("*", "skill_set"):
            r[1] = "'%s'" % r[1]
            r[2] = "'%s'" % r[2]
            if not d.insert("skill_set", r):
                check = True
        
        print "Database client popolato con le entry..."
        for r in d.select("*", "skill_set"):
            print r
        if check:
            print "ERRORE: Alcune skill_set possono non essere stati inseriti!!!"
    else:
        print "Impossibile creare tabella skill_set."
