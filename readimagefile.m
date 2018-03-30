%{
fin = fopen('imageabspath.txt' ,'r');
datas = cell(1 , 2121);
i=1;
while ~feof(fin)
    data = fscanf(fin , '%s' , [1 , 1]);
    datas{i} = data;
    i = i + 1;
end
    
length(datas)
%}

for i=1:length(datas)
    image_filename = datas{i}
    current_img = im2double(imread(image_filename));
end
