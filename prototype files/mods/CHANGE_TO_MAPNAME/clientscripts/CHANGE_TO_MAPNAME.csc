#include clientscripts\_utility;
#include clientscripts\_music;

main()
{
	clientscripts\_load::main();

	clientscripts\CHANGE_TO_MAPNAME_fx::main();

	thread clientscripts\_audio::audio_init(0);
	
	thread clientscripts\CHANGE_TO_MAPNAME_amb::main();
	
	thread waitforclient(0);
}
