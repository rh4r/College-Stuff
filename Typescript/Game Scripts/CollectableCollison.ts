const RUNTIME_OBJS = runtime.objects;
var PLAYER_OBJ = RUNTIME_OBJS.Player.getFirstInstance();

function LogPlayerScore()
{
    if (PLAYER_OBJ != null && PLAYER_OBJ.instVars != null){
        var PLAYER_SCORE = PLAYER_OBJ.instVars;

        for (var item in PLAYER_SCORE){
            if (item == "CurrentScore"){
                console.log("Found item CurrentScore!");
                console.log(PLAYER_SCORE[item]);
            }
        }
    }
}

function SpawnNewCollectable()
{
	var SCORE_COLLECTABLE = RUNTIME_OBJS.Collectable.getFirstInstance()

    if (PLAYER_OBJ != null && SCORE_COLLECTABLE != null){
        var PLAYER_POS_X = (PLAYER_OBJ.x + 750)
		var PLAYER_POS_Y = PLAYER_OBJ.y

		SCORE_COLLECTABLE.setPosition(PLAYER_POS_X, PLAYER_POS_Y );
    }
}

LogPlayerScore()
SpawnNewCollectable()
