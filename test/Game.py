# Import Engine
import sys
sys.path.insert(1, 'src')
import engine

# Import Script
import World
import Move

a = engine.Graphic.Polygon()
a.x = 100
a.y = 100
a.SetNewPoints([(0,0),(100,0),(100,100),(0,100)])
a.Script = Move.Script

engine.world.AddGraphic(a)
engine.world.SetScript(World.World_Script)
# engine.SetWorldScript(World.World_Script)

# Run Game
engine.Active()