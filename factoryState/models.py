from django.db import models
from django.forms import ModelForm

class FactoryState(models.Model):

    def getFields(self):
        return [(field.name, field.value_to_string(self)) for field in FactoryState._meta.fields]

    factoryId = models.IntegerField(default=1)

    #mapping
    var_1ma=models.IntegerField()
    var_2ma=models.IntegerField()
    var_3ma=models.IntegerField()
    var_4ma=models.IntegerField()

    #axis settings
    
    #feed rate
    var_xfr=models.IntegerField()
    var_yfr=models.IntegerField()
    var_zfr=models.IntegerField()
    var_afr=models.IntegerField()

    #max velocity
    var_xvm=models.IntegerField()
    var_yvm=models.IntegerField()
    var_zvm=models.IntegerField()
    var_avm=models.IntegerField()

    #travel
    var_1tr=models.FloatField()
    var_2tr=models.FloatField()
    var_3tr=models.FloatField()
    var_4tr=models.FloatField()

    #step angle
    var_xsa=models.FloatField()
    var_ysa=models.FloatField()
    var_zsa=models.FloatField()
    var_asa=models.FloatField()

    #polarity
    var_1po=models.IntegerField()
    var_2po=models.IntegerField()
    var_3po=models.IntegerField()
    var_4po=models.IntegerField()

    #power mode
    var_1pm=models.IntegerField()
    var_2pm=models.IntegerField()
    var_3pm=models.IntegerField()
    var_4pm=models.IntegerField()
    
    #raw materials in stock
    solettesInHopper=models.IntegerField()  #number of solettes
    tabbingOnSpool=models.IntegerField()  #mm of tabbing
    backingsInHopper=models.IntegerField()  #number of backings
    encapsulantInTub=models.IntegerField()  #ccs of encapsulant

    backingWidth=models.FloatField()  #in mm
    backingLength=models.FloatField() #in mm

    soletteWidth=models.FloatField()  #in mm
    soletteLength=models.FloatField()  # in mm
    soletteThickness=models.FloatField()  # in mm


    hopperPosition=models.FloatField() #in mm, hopperPosition along the axis
    conveyorPosition=models.FloatField() #in mm, conveyorPosition along the axis

    suctionReleaseTime=models.IntegerField()  #in ms, how long you wait after releasing suction, before moving the head
    suctionDelay=models.IntegerField()  #in ms, how long you wait after turning on suction, before moving the head


    #backing dimensions
    tabbingOffset=models.FloatField()
    holeOffset=models.FloatField()
    holeLength=models.FloatField()
    padLength=models.FloatField()
    tabbingConnection=models.FloatField()
    tabbingLength=models.FloatField()  #in mm, the length of tabbing to extend with every solette placement
    tabbingOffset=models.FloatField()

    soletteSpacing=models.FloatField()  #in mm

    halfAdvance=models.FloatField() #in mm, half of the (solette width + solette spacing
    
    tabberPosition=models.FloatField()
    pickPosition=models.FloatField()
    soldererPosition=models.FloatField()
    testPosition=models.FloatField()
    endPosition=models.FloatField()
