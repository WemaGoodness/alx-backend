import kue from 'kue';

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((job) => {
    const jobInstance = queue.create('push_notification_code_3', job)
      .save((err) => {
        if (!err) console.log(`Notification job created: ${jobInstance.id}`);
      });

    jobInstance.on('complete', () => {
      console.log(`Notification job ${jobInstance.id} completed`);
    }).on('failed', (errorMessage) => {
      console.log(`Notification job ${jobInstance.id} failed: ${errorMessage}`);
    }).on('progress', (progress) => {
      console.log(`Notification job ${jobInstance.id} ${progress}% complete`);
    });
  });
};

export default createPushNotificationsJobs;
