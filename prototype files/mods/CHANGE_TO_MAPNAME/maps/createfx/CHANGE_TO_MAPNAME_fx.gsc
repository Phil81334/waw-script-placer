main()
{
	ent = maps\_utility::createOneshotEffect( "fog_thick" );
	ent.v[ "origin" ] = ( 488, 0, 48 );
	ent.v[ "angles" ] = ( 270, 0, 0 );
	ent.v[ "fxid" ] = "fog_thick";
	ent.v[ "delay" ] = -15; 
}
