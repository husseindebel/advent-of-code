#!/usr/bin/perl -w
use List::Util qw[min max];

$total_cost = 0;
$wrap = 0;

while ($line = <>){
	if ($line =~ /(\d+)x(\d+)x(\d+)/){
		$length = $1;
		$width = $2;
		$height = $3;
		$max_number = max($length, $width, $height);
		if ($max_number == $length){
			$wrap = get_wrapper($width, $height);
		} elsif ($max_number == $width){
			$wrap = get_wrapper($height, $length);
		} else {
			$wrap = get_wrapper($width, $length);
		}	
		$total_cost += $wrap + $length*$width*$height;
	}
}

sub get_wrapper {
	($a, $b) = @_;
	return 2*$a+2*$b;
}
print $total_cost, "\n";
