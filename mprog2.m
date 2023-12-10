% read in data from c output file
% Each of these files were creating using the Python script and the
% respective language
data = fileread('input.txt');
dataC = fileread('c_output.txt');
dataH = fileread('haskell_output.txt');
dataP = fileread('prolog_output.txt');

% convert string to numbers then into unsigned chars
datanum = uint8(str2num(data));
datanumC = uint8(str2num(dataC));
datanumH = uint8(str2num(dataH));
datanumP = uint8(str2num(dataP));

% resize into 2d matrix
resize_matrix = reshape(datanum, 92,92);
resize_matrixC = reshape(datanumC, 92,92);
resize_matrixH = reshape(datanumH, 92,92);
resize_matrixP = reshape(datanumP, 92,92);

% Creates a figure to display the images
figure;

% Splits the figure into 2x2 and displays each image in a quadrant
subplot(2,2, 1);
imshow(resize_matrix);
title('Original Image');

subplot(2,2,2);
imshow(resize_matrixC);
title('C: Black and White');

subplot(2,2,3);
imshow(resize_matrixH);
title('Haskell: Inverted Color')

subplot(2,2,4);
imshow(resize_matrixP);
title('Prolog, Flipped Image')

pause(20);

exit;
