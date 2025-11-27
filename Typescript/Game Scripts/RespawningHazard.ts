const RUNTIME_OBJS = runtime.objects
const PLAYER_OBJ = RUNTIME_OBJS.Player.getFirstInstance()
const COLLECTABLE_OBJ = RUNTIME_OBJS.Collectable.getFirstInstance()
const HAZARD_OBJ = RUNTIME_OBJS.HitObject.getFirstInstance()

function ScheduledSpawnNewCollectable()
{
    if (PLAYER_OBJ && COLLECTABLE_OBJ && HAZARD_OBJ){
        var PLAYER_POS_X = (PLAYER_OBJ.x + 750)
		var PLAYER_POS_Y = PLAYER_OBJ.y
		var HAZARD_POS = HAZARD_OBJ.x
		var COLLECTABLE_POS = COLLECTABLE_OBJ.x
		
		if ((HAZARD_POS - COLLECTABLE_POS ) >= 30){
			console.log("TODO");
		}

		COLLECTABLE_OBJ.setPosition(PLAYER_POS_X, PLAYER_POS_Y );
    }
}

function DetermineDistance()
{
	if (PLAYER_OBJ && COLLECTABLE_OBJ)
	{
		var PLAYER_POS = PLAYER_OBJ.x;
		var COLLECTABLE_POS = COLLECTABLE_OBJ.x;

		if (COLLECTABLE_POS < PLAYER_POS){
			ScheduledSpawnNewCollectable();
			console.log("COLLECTABLE OUT OF BOUNDS, SPAWNING NEW")
		}
	}
}

DetermineDistance();
