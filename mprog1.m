% Reads the image
picture_rgb = imread('mickey.png');

% converts the image from colored to grayscale
picture = im2gray(picture_rgb);

% Reshape the image into a 1D array
picture_1d = reshape(picture, 1, []);

% Write data to a file
dlmwrite('input.txt', picture_1d, 'delimiter', ' ');

