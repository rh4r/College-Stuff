const RUNTIME_ITEMS = runtime.objects;
var HealthHeart3 = runtime.objects.Healthbar3.getFirstInstance();
var HealthHeart2 = runtime.objects.Healthbar2.getFirstInstance();
var HealthHeart1 = runtime.objects.Healthbar1.getFirstInstance();

function MainLogic(){
	if (HealthHeart3 != null){
		if (HealthHeart2 != null)
		{
			if (HealthHeart1 != null){
				if (HealthHeart1.isVisible && HealthHeart2.isVisible == false){
					HealthHeart1.isVisible = false;
				}
				if (HealthHeart2.isVisible && HealthHeart3.isVisible == false){
					HealthHeart2.isVisible = false;
				}
				if (HealthHeart3.isVisible && HealthHeart2.isVisible){
					HealthHeart3.isVisible = false;
				}
			}
		}
	}
}

MainLogic()
