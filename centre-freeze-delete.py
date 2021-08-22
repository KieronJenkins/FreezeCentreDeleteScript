import maya.cmds as cmds

# Made using Python. This script changes Selects all objects in a scene, centres their pivots, freezes their transforms and deletes history.

def centre_freeze_delete():
    cmds.select( all=True ) # Delete this if you don't want to Select Everything
    cmds.xform(centerPivots=True) # Delete this if you don't want to Centre Pivots
    cmds.makeIdentity( apply=True, t=1, r=1, s=1 ) # Delete this if you don't want to Freeze Transforms
    cmds.delete(constructionHistory = True) # Delete this if you don't want to Delete History
    print("Centred, Frozen and Deleted") # Delete this if you don't want to print anything in console afterwards
    
    
centre_freeze_delete()


# Set Up: Create a custom button in your shelf editor then Set to Python and then copy paste the above in
