U
    T��_		  �                   @   s�   d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dl mZmZm	Z	 dd� Z
dd� Zdd� Zd	d
� Zdd� Zdd� Ze�  dS )�    N)�TelegramClient�sync�utilsc                  C   s�   d} d}t d| |��� }td�}zttd��}W n tk
rH   d}Y nX td�}t|�D ]:}|�||� tj�	d�
|d	 |�� tj��  td
� qZd S )Ni	� Z 9a9e8bfa65a1374b4cce8e855b069071�client�TST > set USERNAME/ID �santet > set COUNT �d   �TST > set MESSAGE �$[1000D[*] Sent {} messages to {}...�   �
[!] Done ... !!
)r   �start�input�int�
ValueError�range�send_message�sys�stdout�write�format�flush�print)�api_id�api_hashr   �target�count�urmsg�x� r   �pppp.py�main   s      

r!   c            	      C   s�   t d�} td� t d�}| }|}td||��� }t d�}ztt d��}W n tk
r`   d}Y nX t d�}t|�D ]:}|�||� tj	�
d	�|d
 |�� tj	��  td� qrd S )NzEnter your Telegram Id >> � zEnter your Telegram Hash >> r   r   r   r   r	   r
   r   r   )r   r   r   r   r   r   r   r   r   r   r   r   r   )	ZenterZrespor   r   r   r   r   r   r   r   r   r    �your   s"      

r#   c                   C   s   t d� d S )Nz,Enter your details and start your spam tool �r   r   r   r   r    �help%   s    r%   c                   C   s,   t �d� t �d� t �d� t �d� d S )NZcdz&git clone https:github.com/isuruwa/TSTzcd TSTzpython tst.py)�os�systemr   r   r   r    �update(   s    


r(   c                   C   s   t d� t d� t d� d S )Nz[35mCREATED BY ISURUWA.z[36mFollow me on GithubzJ[35mFollow me on facebook - https://www.facebook.com/isuru.umayanga.37819r$   r   r   r   r    �about/   s    r)   c                  C   s�   t �d� t �d� td� td� td� td� td� td� td	� td� td
�} | dkrjt�  | dkrxt�  | dkr�t�  | dkr�t�  | dkr�t�  | dkr�t	�  d S )N�clearztoilet -f mono12 -F gay "TST"z([1;32m     Telegram [35mSpam [36mToolr"   z[31m1.Start Bomberz)[1;32m2.Create Your Own Telegram Bomber z[33m3.Helpz[36m4.Updatez[35m5.Aboutz[36mEnter your option >>> �1�2�3�4�5)
r&   r'   r   r   r!   r#   r%   r(   r)   �prog)Zaskr   r   r    r0   5   s.    

r0   )Ztelethonr&   r   �timeZsocketZrandomZrequestsr   r   r   r!   r#   r%   r(   r)   r0   r   r   r   r    �<module>   s   0$