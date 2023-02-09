class Solution:
    def reformatDate(self, date: str) -> str:
        opt = []
        
        month = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        
        date = date.split(" ")
        opt.append(date[2])
        opt.append(month[date[1]])
        
        day = date[0]
        day = day[:-2]
        
        if len(day) == 1:
            opt.append("0" + day)
        else:
            opt.append(day)
                
        return "-".join(opt)
            
            
        
        
        
        
        