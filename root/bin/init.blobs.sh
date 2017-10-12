#!/system/bin/sh

SRCPATH=/vendor/etc/firmware/
DSTPATH=/system/etc/firmware/
FULL=$(strings /dev/block/platform/msm_sdcc.1/by-name/TA | grep glte)
CODENAME=$(echo $FULL | cut -d "_" -f 1)
VARIANT=$(echo $FULL | cut -d "_" -f 2)

echo "full: $FULL"
echo "variant: $VARIANT"
echo "codename: $CODENAME"

echo "Remounting system rw"
mount -o rw,remount /system

for set in adsp modem ; do
	echo "set: ${set}"
	for f in `find $SRCPATH -type f -name "${set}_${CODENAME}_${VARIANT}*" | sort` ; do
		ext=$(echo $f | cut -d'.' -f2)
		DSTFILE="${DSTPATH}${set}.${ext}"
		if [ ! -e $DSTFILE ]
		then
			ln -sv $f ${DSTFILE}
		else
			echo "${DSTFILE} already exist. Skipping."
		fi
	done

done

if [[ "$VARIANT" = "dsds" ]]
then
	cp -v /system/build.prop.dual /system/build.prop
fi

echo "Remounting system ro"
mount -o ro,remount /system

