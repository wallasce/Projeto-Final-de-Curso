from datetime import datetime, timedelta
from SQLiteManager import SQLiteManager

class formaterData:
    def __init__(self) -> None:
        self.formatDateMS = "%Y-%m-%d %H:%M:%S.%f"
        self.formatDate = "%Y-%m-%d %H:%M:%S"
        pass

    def getFormatedData(self,  data : list[tuple]) -> None:
        dataListFormated = self.generateDatatoEachSecond(data)
        return self.transformListToString(dataListFormated)

    # Check if the diference between date1 and date2 is one second.
    def deltaIsOneSecond(self, date1 : str, date2 : str) -> bool:
        datetime1 = datetime.strptime(date1, self.formatDateMS)
        datetime2 = datetime.strptime(date2, self.formatDateMS)

        strdate1 = datetime1.strftime(self.formatDate)
        strdate2 = (datetime2 + timedelta(seconds=1)).strftime(self.formatDate)

        return strdate1 == strdate2
    
    # Add a second in date. Return String Format
    def addOneSecond(self, date) -> str:
        dateVar = datetime.strptime(date, self.formatDateMS)

        return (dateVar + timedelta(seconds=1)).strftime(self.formatDateMS)
    
    # Garants data for each second stored.
    def generateDatatoEachSecond(self, dataList : list[tuple]) -> list[tuple]:
        dataListFormated = []   
        dataListFormated.append(dataList[0])
        count = 1
        while(True):
            if (count == len(dataList)):
                break
                
            if (self.deltaIsOneSecond(dataList[count][0], dataListFormated[-1][0])):
                dataListFormated.append(dataList[count])
                count += 1
            else:
                newData = self.addOneSecond(dataListFormated[-1][0])
                dataListFormated.append((newData, dataListFormated[-1][1]))

        return dataListFormated
    
    def transformListToString(self, dataList : list[tuple]) -> str:
        dataStr = ''
        
        for data in dataList:
            dataStr += str(data) + '\n'

        return dataStr
    
    
sqlConnection = SQLiteManager('temperature_history.sql')
answer = sqlConnection.selectDataFrom('2_5')
sqlConnection.stopConnection()

test = formaterData()
print(test.getFormatedData(answer))