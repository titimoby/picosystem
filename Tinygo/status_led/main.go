package main

import (
	"machine"
	"time"
)

func main() {
	ledGreen := machine.GP13
	ledRed := machine.GP14
	ledBlue := machine.GP15
	ledGreen.Configure(machine.PinConfig{Mode: machine.PinOutput})
	ledRed.Configure(machine.PinConfig{Mode: machine.PinOutput})
	ledBlue.Configure(machine.PinConfig{Mode: machine.PinOutput})
	for {
		ledGreen.Low()
		ledRed.Low()
		ledBlue.Low()
		time.Sleep(time.Millisecond * 500)

		ledGreen.High()
		ledRed.Low()
		ledBlue.Low()
		time.Sleep(time.Millisecond * 500)

		ledGreen.Low()
		ledRed.High()
		ledBlue.Low()
		time.Sleep(time.Millisecond * 500)

		ledGreen.Low()
		ledRed.Low()
		ledBlue.High()
		time.Sleep(time.Millisecond * 500)
	}
}
