#from fuzzywuzzy import *
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



choices = ["PerkinElmer, Inc.", "SAP Global Marketing, Inc.", "14693 Edelman", "TOYOTA MOTOR CORPORATION Family : Toyota Canada Inc."]

result = process.extract("TOYOTA MOTOR CORPORATION Family : Toyota Sweden AB", choices, limit=1)
result2 = process.extract("PerkinElmer", choices, limit=2)
result3 = process.extract("Mio!Global", choices, limit=1)

print result
print result2

print result3
