FROM python:3.6-onbuild

ARG TIMEZONE
ENV USER_HOME /root
ENV APP_FOLDER /usr/src/app

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    apt-get install -y \
        cron \
        nano \
        gettext

ADD ./__files/.gitconfig ${USER_HOME}
ADD ./__files/.bashrc ${USER_HOME}
ADD ./__files/git-completion.bash ${USER_HOME}

RUN ln -snf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && echo ${TIMEZONE} > /etc/timezone && 2> /dev/null \
    echo "127.0.0.1 tshirter.local" >> /etc/hosts \
    pip install --upgrade pip

ADD ./requirements.txt ${APP_FOLDER}/

RUN pip install -r requirements.txt
