U
    �ɗ_�
  �                   @   s�   d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dl mZmZm	Z	 dd� Z
dd� Zdd� Zd	d
� Zdd� Zdd� Ze�  dS )�    N)�TelegramClient�sync�utilsc                  C   s�   d} d}t d| |��� }td�}zttd��}W n tk
rH   d}Y nX td�}t|�D ]:}|�||� tj�	d�
|d	 |�� tj��  td
� qZd S )Ni	� Z 9a9e8bfa65a1374b4cce8e855b069071�client�TST > set USERNAME/ID �santet > set COUNT �d   �TST > set MESSAGE �$[1000D[*] Sent {} messages to {}...�   �
[!] Done ... !!
)r   �start�input�int�
ValueError�range�send_message�sys�stdout�write�format�flush�print)�api_id�api_hashr   �target�count�urmsg�x� r   �tool.py�main   s      

r!   c            	      C   s�   t d�} td� t d�}| }|}td||��� }t d�}ztt d��}W n tk
r`   d}Y nX t d�}t|�D ]:}|�||� tj	�
d	�|d
 |�� tj	��  td� qrd S )NzEnter your Telegram Id >> � zEnter your Telegram Hash >> r   r   r   r   r	   r
   r   r   )r   r   r   r   r   r   r   r   r   r   r   r   r   )	ZenterZrespor   r   r   r   r   r   r   r   r   r    �your   s"      

r#   c                   C   s,   t d� t d� t d� t d� t d� d S )Nz,1.Enter the details and start the spam tool r"   z�2.If you want to create your own Telegram Spam Bot , go to https://my.telegram.org $ get your telegram api id and hash. Then select the 2nd option from the tool and Enter your data & log to your telegram account . Then it is YOURS !!!z:3.Find me on https://www.facebook.com/isuru.umayanga.37819�r   r   r   r   r    �help%   s
    r%   c                   C   s6   t �d� t �d� t �d� t �d� t �d� d S )NZcdz
rm -rf TSTz(git clone https://github.com/isuruwa/TSTzcd TSTzpython tst.py)�os�systemr   r   r   r    �update,   s
    



r(   c                   C   s   t d� t d� t d� d S )Nz[35mCREATED BY ISURUWA.z[36mFollow me on GithubzJ[35mFollow me on facebook - https://www.facebook.com/isuru.umayanga.37819r$   r   r   r   r    �about4   s    r)   c                  C   s�   t �d� t �d� td� td� td� td� td� td� td� td	� td
� td� td�} | dkrzt�  | dkr�t�  | dkr�t�  | dkr�t�  | dkr�t�  | dkr�t	�  d S )N�clearztoilet -f mono12 -F gay "TST"z([1;32m     Telegram [35mSpam [36mToolr"   z[31m#CODED BY ISURUWAz[31m1.Start Bomberz)[1;32m2.Create Your Own Telegram Bomber z[33m3.Helpz[36m4.Updatez[35m5.Aboutz[36mEnter your option >>> �1�2�3�4�5)
r&   r'   r   r   r!   r#   r%   r(   r)   �prog)Zaskr   r   r    r0   :   s2    

r0   )Ztelethonr&   r   �timeZsocketZrandomZrequestsr   r   r   r!   r#   r%   r(   r)   r0   r   r   r   r    �<module>   s   0&