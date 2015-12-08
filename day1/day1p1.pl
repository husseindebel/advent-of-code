#!/usr/binperl -w

$floor_number = 0;

while ($line = <>){
	chomp $line;
	foreach $instruction (split //, $line){
		if ($instruction eq "("){
			$floor_number++;
		} else {
			$floor_number--;
		}
	}
}

print $floor_number, "\n";

