# Pi blink

This is sample code to test deployment and builds in Armainer. It is not an application to keep. When a build reaches the machine, switch the fleet to your own repository.

The sample blinks the green activity LED on a Raspberry Pi once a second. The LED name is `ACT`.

## Board families

Use this sample only on a Raspberry Pi fleet:

- Raspberry Pi 3
- Raspberry Pi 4, Pi 400, Pi 5, Compute Module 4, and Compute Module 5

These boards run Pi OS and expose the activity LED as `ACT`.

Do not use this sample on these fleets. The LED path is different, and it has not been tested on that hardware:

- Orange Pi 5, 5B, 5 Plus, and 5 Pro
- Banana Pi BPI-M5
- Generic x86 mini PC

For those fleets, start with [Armainer/sample-hello](https://github.com/Armainer/sample-hello).

## Run it

In a Raspberry Pi fleet, build `https://github.com/Armainer/sample-pi-blink.git` on branch `main`.

The container needs access to the LED, so the compose file sets `privileged: true`. The activity LED stops showing card activity while this container runs, and returns to that job when the container stops.

## Licence

MIT. You can use, change, and ship this sample, including in your own product. Keep the copyright notice from `LICENSE` in copies of the code.
