from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector
"""@package docstring
SQL server connector disigned to connect to the server to deal with sending data

More details.
"""
class SQLConnector():
	"""Documentation for a class.
    """
	"""SQL connection connector to the presetted MySQL serevr

	"""
    def __init__(self):
		"""The constructor."""
        self.data=""
			"""Main data progress data"""
        self.NamePerson=""
			"""Name of person"""
        self.Lessondata=""
			"""Lessonname and number"""

    def onLoad(self):
		"""The Destroctor."""
        #put initialization code here
        pass

    def onUnload(self):
		"""SQLclass clean-up.
		
		More details.
		"""
        #put clean-up code here
        pass

    def onInput_onStart(self):
		"""SQLclass Main program to send the needed data.
	
		cnx =    mysql.connector.connect(user='Naobotuser',
		                          		   password='Naobot1',
		                                  host='83.128.154.70',
		                                  database='nao_progress')"""
        cnx =    mysql.connector.connect(user='Naobotuser',
                              password='Naobot1',
                              host='83.128.154.70',
                              database='nao_progress')
        cursor = cnx.cursor()
        
        if self.write:
            
    
            now = datetime.now().date()
    
            add_employee = ("INSERT INTO progresslog "
                           "(Lognumber, NamePerson, Lesson, Progress) "
                           "VALUES (%s, %s, %s, %s)")
    
            data_employee = (now, self.NamePerson,self.Lessondata, self.data)
            # Insert new employee
            cursor.execute(add_employee, data_employee)
            # Make sure data is committed to the database
            cnx.commit()
        
        
        #query = ("SELECT Lognumber, NamePerson, Lesson, Progress FROM progresslog ")


        #cursor.execute(query)

		#for (Lognumber, NamePerson, Lesson, Progress) in cursor:
		#	print("{} {} has exicuted {} with these results:{}".format(Lognumber, NamePerson, Lesson, Progress))
        
        
        cursor.close()
        cnx.close()
        self.onInput_onStop() #activate the output of the box
        pass

    def onInput_onStop(self):
		"""SQLclass destructor."""
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box

    def onInput_Data(self, p):
		"""SQLclass Data reciver of how goed the person is doing"""
        self.data=p
        pass

    def onInput_NamePerson(self, p):
		"""SQLclass Data recieves the datanumber or persons name"""
        self.NamePerson=p
        pass

    def onInput_Lessondata(self, p):
		"""SQLclass Data recieves the Lesson number"""
        self.Lessondata=p
        pass
    
"""@file SQLInternettest.py"""