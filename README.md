# computer-vision-project

Final group project for COMP4102 at Carleton University.

## Group Members

- Joshua Arts
- Bimal Bhagrath
- Vikram Bombhi
- Drew Suitor


## TODO
- make 

## DONE
- retrieve information from image
- encoding information into hex
- creating images from hex
- should be able to go from barcode -> hex value
- should be able to go from hex value -> barcode
- set up server to send and receive information from iOS app
- find barcode in "noisy" image

### Stretch TODO
- map hex value of an image to some sort of useable information (link, file, some piece of data) that can be returned by the server to a client
- decode "messy" images, like one taken from a smartphone, images that aren't "perfect"

### Spec Draft

Barcode will encode single hex digits (0…f) using the following rules:

- The bars (from the example image) represent the following hex characters from left to right
    - (Orientation bar) 0 1 2 3 4 5 6 7 8 9 A B C D E F
- The __orientation bar__ is the longest bar in the image. This bar is to be placed at the far left and the rest of the bars are read from left to right. The orientation bar will help determine the correct orientation of the barcode.
- Assume the orientation bar’s height represents the height of the frame. All __data bars__ will have heights that are `(x/10 * frame height)` where `x` is `base_10(hex) // 2`
    - i.e. the height of bar `B` will be `base_10(B)` which is 11 then `11 // 2` which is 5, so (5/10 * frame_height)
- The data bars will either start at the top of the frame or end at the bottom of the frame, causing a scissor like appearance. If the `base_10(hex) % 2 === 0` then the bar starts at the top of the frame, else it ends at the bottom.
    - i.e. bar `B` has base_10 = 11, 11 % 2 = 1, therefore it will end at the bottom of the frame
- The orientation bar is 2x the width of the data bars, and the data bars must have 2x the data bar width of spacing between them. Actual bar pixel sizes does not matter as long as constraints are met.

