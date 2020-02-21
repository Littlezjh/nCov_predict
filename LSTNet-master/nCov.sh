D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_zhejiang.txt --save save/nCov.pt --skip -7 --output_fun Linear --normalize 0
D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_hubei.txt --save save/nCov.pt --skip -7 --output_fun Linear --norm
alize 0 --horizon 3

D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_zhejiang.txt --save save/zhejiang_200.pt --skip -7 --epochs 300 --output_fun Linear --normalize 0 --horizon 1 --window 5 --CNN_kernel 3

D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_hubei.txt --save save/hubei.pt --skip -7 --output_fun Linear --normalize 0 --horizon 1 --window 5 --CNN_kernel 3

D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_hubei.txt --save save_2/hubei_1.pt --horizon 1 --skip -7 --output_fun Linear --normalize 0  --window 5 --CNN_kernel 3
D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_hubei.txt --save save_2/hubei_2.pt --horizon 2 --skip -7 --output_fun Linear --normalize 0  --window 5 --CNN_kernel 3
D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_hubei.txt --save save_2/hubei_3.pt --horizon 3 --skip -7 --output_fun Linear --normalize 0  --window 5 --CNN_kernel 3
D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_hubei.txt --save save_2/hubei_4.pt --horizon 4 --skip -7 --output_fun Linear --normalize 0  --window 5 --CNN_kernel 3
D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_hubei.txt --save save_2/hubei_5.pt --horizon 5 --skip -7 --output_fun Linear --normalize 0  --window 5 --CNN_kernel 3

D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_zhejiang.txt --save save_2/zhejiang_1.pt --horizon 1 --skip -7 --output_fun Linear --normalize 0  --window 5 --CNN_kernel 3
D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_zhejiang.txt --save save_2/zhejiang_2.pt --horizon 2 --skip -7 --output_fun Linear --normalize 0  --window 5 --CNN_kernel 3
D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_zhejiang.txt --save save_2/zhejiang_3.pt --horizon 3 --skip -7 --output_fun Linear --normalize 0  --window 5 --CNN_kernel 3
D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_zhejiang.txt --save save_2/zhejiang_4.pt --horizon 4 --skip -7 --output_fun Linear --normalize 0  --window 5 --CNN_kernel 3
D:\Software\Anaconda\envs\pytorch\python.exe main.py  --data data/data_zhejiang.txt --save save_2/zhejiang_5.pt --horizon 5 --skip -7 --output_fun Linear --normalize 0  --window 5 --CNN_kernel 3
