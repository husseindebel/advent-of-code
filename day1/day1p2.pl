#!/usr/binperl -w

$floor_number = 0;
$position = 0;
while ($line = <>){
	chomp $line;
	foreach $instruction (split //, $line){
		$position++;
		if ($instruction eq "("){
			$floor_number++;
		} else {
			$floor_number--;
		}
		if ($floor_number == -1){
			print $position, "\n";
			exit 1;
		}
	}
}

print $floor_number, "\n";

