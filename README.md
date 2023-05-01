# image-steganography

Steganography-data is hidden in plain sight

Steganography is the art and science of embedding secret messages in cover message in such a way that no one, apart from sender and intended recipient, suspects the existamce of the mssg

Steganography-Steganos(concealed or hidden)+graphen(drawing/writing)

cover media-means by which u are hiding image
steganography types:text,image,audio,video,network,email

Characteristics of Steganographic techniques:transparency(there must be no distortion in image after we hide the mssg),robustness(the image does not loose info even if the media undergoes some damage like cropping,filtering),tamper resistance(the ability of a device to defend against a threat that has the objective to compromise the device and or the data processed by the device)

LSB steganography-least significant bit steganography
if we change most significant bit, it will have a larger imapct on final value. If we change LSB, the impact on final value is very less.

For example:
Value:255=1111 1111
Value after changing msb:0111 1111=127 so change in bytes is 99.9999%
value after changing lsb:1111 1110=254 so change in bytes is 0.000002%

lsb steganography involves overwriting the bit with the lowest arithmetic value
